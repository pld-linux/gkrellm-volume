Summary:	volume plugin for gkrellm
Summary(pl):	Wtyczka kontroli g³o¶no¶ci dla gkrellm
Summary(pt_BR):	Plugin gkrellm para controle do volume de dispositivos de som
Name:		gkrellm-volume
Version:	0.8
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://gkrellm.luon.net/files/volume-%{version}.tar.gz
Requires:	gkrellm >= 1.0.2
BuildRequires:	gkrellm-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A GKrellM plugin wich allows you to control the (OSS) mixer devices of
you choice.

%description -l pl
Wtyczka GKrellM pozwalaj±ca kontrolowaæ ustawienia miksera (OSS).

%description -l pt_BR
Plugin gkrellm para controle do volume de dispositivos de som (OSS).

%prep
%setup -q -n volume

%build
%{__make} \
	CC="%{__cc} %{rpmcflags} `gtk-config --cflags` `imlib-config --cflags-gdk`"

%install
rm -rf $RPM_BUILD_ROOT

install -D volume.so %{buildroot}%{_libdir}/gkrellm/plugins/volume.so

gzip -9nf README Changelog

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/gkrellm/plugins/volume.so
