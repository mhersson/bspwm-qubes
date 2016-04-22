Name:		sxhkd
Version:	0.5.6
Release:	1%{?dist}
Summary:	Simple X hotkey daemon

License:	BSD
URL:		https://github.com/baskerville/sxhkd
Source0:	https://github.com/baskerville/sxhkd/archive/%{version}.tar.gz

BuildRequires:	libxcb-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-keysyms-devel
Requires:	libxcb
Requires:	xcb-util-keysyms


%description
sxhkd is a simple X hotkey daemon with a powerful and compact configuration syntax.

%prep
%setup -q


%build
make VERBOSE=1 %{?_smp_mflags} CFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
%make_install PREFIX="%{_prefix}"


%files
%license LICENSE
%{_bindir}/%{name}
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.1.gz


%changelog

* Sat Apr 16 2016 Morten Hersson <mhersson@gmail.com>
- Initial release
