Summary:	Sound volume plugin for gkrellm
Summary(pl):	Wtyczka kontroli g³o¶no¶ci dla gkrellm
Summary(pt_BR):	Plugin gkrellm para controle do volume de dispositivos de som
Name:		gkrellm-volume
Version:	2.1.13
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://gkrellm.luon.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	d9f4c36d7fdf9c9f755c99f742b573c4
Patch0:		%{name}-i18n.patch
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GKrellM plugin wich allows you to control the mixer devices of your
choice.

%description -l pl
Wtyczka GKrellM pozwalaj±ca kontrolowaæ ustawienia miksera.

%description -l pt_BR
Plugin gkrellm para controle do volume de dispositivos de som.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	GKRELLM_INCLUDE=`pkg-config --cflags gkrellm` \
	PLUGIN_DIR=%{_libdir}/gkrellm2/plugins \
	LOCALEDIR=%{_datadir}/locale \
	CC="%{__cc} \$(FLAGS) %{rpmcflags}" \
	enable_nls=1 \
	enable_alsa=1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

%{__make} install \
	PLUGIN_DIR=$RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins \
	LOCALEDIR=$RPM_BUILD_ROOT%{_datadir}/locale \
	INSTALL_PROGRAM="install" \
	enable_nls=1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/volume.so
