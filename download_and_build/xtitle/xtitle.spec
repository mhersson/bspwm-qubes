Name:		xtitle
Version:	0.3
Release:	1%{?dist}
Summary:	Outputs X window titles

License:	Public Domain
URL:		https://github.com/baskerville/xtitle
Source0:	https://github.com/baskerville/xtitle/archive/%{version}.tar.gz

BuildRequires:	libxcb-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-wm-devel

%description
If arguments are given, outputs the title of each arguments, otherwise outputs the title of the active window and continue to output it as it changes if the snoop mode is on.

%define debug_package %{nil}

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


%changelog

* Sat Apr 16 2016 Morten Hersson <mhersson@gmail.com>
- Initial release
