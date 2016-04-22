Name:		bspwm
Version:	0.9.1
Release:	1%{?dist}
Summary:	A tiling window manager based on binary space partitioning
Group:		User Interface/Desktops

License:	BSD
URL:		https://github.com/baskerville/bspwm
Source0:	https://github.com/baskerville/bspwm/archive/%{version}.tar.gz

BuildRequires:	libxcb-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	desktop-file-utils
Requires: libxcb
Requires: xcb-util
Requires: xcb-util-wm


%description
bspwm is a tiling window manager that represents windows as the leaves of a
full binary tree.

It only responds to X events, and the messages it receives on a dedicated
socket.

bspc is a program that writes messages on bspwm's socket.

bspwm doesn't handle any keyboard or pointer inputs: a third party program
(e.g. sxhkd) is needed in order to translate keyboard and pointer events to
bspc invocations.


%prep
%setup -q


%build
make VERBOSE=1 %{?_smp_mflags} CFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
%make_install PREFIX="%{_prefix}"


%check
desktop-file-validate %{buildroot}/%{_datadir}/xsessions/%{name}.desktop


%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/bspc
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/bspc.1.gz
%{_datadir}/bash-completion/completions/bspc
%{_datadir}/zsh/site-functions/_bspc
%{_datadir}/xsessions/%{name}.desktop


%changelog
* Tue Mar 15 2016 Oles Pidgornyy <pidgornyy@informatik.uni-frankfurt.de> - 0.9.1-1
- Update to 0.9.1
- Fix compliance to freedesktop specifications

* Sat Mar 12 2016 Oles Pidgornyy <pidgornyy@informatik.uni-frankfurt.de> - 0.9-1
- Initial release
