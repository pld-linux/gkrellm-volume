Summary:	volume plugin for gkrellm
Summary(pl):	Wtyczka kontroli głośności dla gkrellm
Summary(pt_BR):	Plugin gkrellm para controle do volume de dispositivos de som
Name:		gkrellm-volume
Version:	2.1.8
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://gkrellm.luon.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	1be6ea5bdccda735ff9c058703889eb3
Requires:	gkrellm >= 2.0.4
BuildRequires:	gkrellm-devel
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GKrellM plugin wich allows you to control the (OSS) mixer devices of
you choice.

%description -l pl
Wtyczka GKrellM pozwalająca kontrolować ustawienia miksera (OSS).

%description -l pt_BR
Plugin gkrellm para controle do volume de dispositivos de som (OSS).

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D volume.so %{buildroot}%{_libdir}/gkrellm2/plugins/volume.so

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/volume.so
