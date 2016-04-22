Name:		sutils
Version:	f35ea44
Release:	1%{?dist}
Summary:	Small command-line utilities

License:	Custom
URL:		https://github.com/baskerville/sutils
Source0:	https://github.com/baskerville/sutils/archive/%{version}.tar.gz

BuildRequires:	alsa-lib-devel

%description
Small command-line utilities

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
%{_bindir}/battery
%{_bindir}/clock
%{_bindir}/essid
%{_bindir}/exist
%{_bindir}/narg
%{_bindir}/temp
%{_bindir}/uq
%{_bindir}/volume


%changelog

* Sat Apr 16 2016 Morten Hersson <mhersson@gmail.com>
- Initial release
