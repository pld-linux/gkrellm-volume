Name: gkrellm-volume
Version: 0.8
Release: 2cl
Summary: volume plugin for gkrellm
Summary(pt_BR): Plugin gkrellm para controle do volume de dispositivos de som
Summary(es): volume plugin for gkrellm
License: GPL
Group: X11
Group(pt_BR): X11
Group(es): X11
Source:	http://gkrellm.luon.net/files/volume-%{version}.tar.gz
Requires: gkrellm >= 1.0.2
BuildRequires: gkrellm-devel, gtk+-devel, imlib-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
A GKrellM plugin wich allows you to control the (OSS) mixer devices
of you choice.

%description -l pt_BR
Plugin gkrellm para controle do volume de dispositivos de som (OSS).

%description -l es
A GKrellM plugin wich allows you to control the (OSS) mixer devices of you
choice.

%prep
%setup -q -n volume

%build
CFLAGS="%{optflags}" make

%install
rm -rf %{buildroot}
install -D -m644 volume.so %{buildroot}%{_libdir}/gkrellm/plugins/volume.so

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README Changelog
%{_libdir}/gkrellm/plugins/volume.so

%changelog
* Sat Nov 10 2001 Claudio Matsuoka <claudio@conectiva.com>
+ gkrellm-volume-0.8-2cl
- fixed doc permissions

* Thu Nov 30 2000 Claudio Matsuoka <claudio@conectiva.com>
+ gkrellm-volume-0.8-1cl
- package created
