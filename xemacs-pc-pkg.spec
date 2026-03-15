Summary:	PC style interface emulation
Summary(pl.UTF-8):	Emulacja interfejsu w stylu PC
Name:		xemacs-pc-pkg
%define 	srcname	pc
Version:	1.30
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/pub/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	af2f1fadc1dd00b5aa16d2bc34e3c6c9
URL:		https://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PC style interface emulation.

%description -l pl.UTF-8
Emulacja interfejsu w stylu PC.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/*
