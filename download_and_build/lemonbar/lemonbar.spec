Name:		lemonbar
Version:	a43b801
Release:	1%{?dist}
Summary:	lemonbar - Featherweight lemon-scented bar

License:	MIT
URL:		https://github.com/krypt-n/bar
Source0:	https://github.com/krypt-n/bar/archive/%{version}.tar.gz

BuildRequires: libXft-devel
BuildRequires: libxcb-devel
BuildRequires: libX11-devel
Requires: libxcb
Requires: libXft
Requires: libX11


%description
bar ain't recursive - A lightweight xcb based bar. This is a fork that supports fontconfig

%prep
%setup -q


%build
make %{?_smp_mflags}



%install
rm -rf %{buildroot}
%make_install PREFIX="%{_prefix}"


%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz


%changelog

* Sat Apr 16 2016 Morten Hersson <mhersson@gmail.com>
- Initial release
