Summary:	PC style interface emulation
Summary(pl):	Emulacja interfejsu w stylu PC
Name:		xemacs-pc-pkg
%define 	srcname	pc
<<<<<<< xemacs-pc-pkg.spec
<<<<<<< xemacs-pc-pkg.spec
<<<<<<< xemacs-pc-pkg.spec
<<<<<<< xemacs-pc-pkg.spec
Version:	1.17
=======
Version:	1.18
>>>>>>> 1.10
=======
Version:	1.19
>>>>>>> 1.11
=======
Version:	1.20
<<<<<<< xemacs-pc-pkg.spec
>>>>>>> 1.12
Release:	1
=======
Release:	2
>>>>>>> 1.14
=======
Version:	1.21
Release:	1
>>>>>>> 1.15
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PC style interface emulation.

%description -l pl
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
