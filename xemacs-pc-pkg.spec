Summary:	PC style interface emulation
Summary(pl):	Emulacja interfejsu w stylu PC
Name:		xemacs-pc-pkg
%define 	srcname	pc
Version:	1.16
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
URL:		http://www.xemacs.org
Source0:	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg

%description
PC style interface emulation.

%description -l pl 
Emulacja interfejsu w stylu PC.

%package el
Summary:	PC style interface emulation. This package contains .el files
Summary(pl):	PC style interface emulation. Pliki ¿ród³owe .el
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description el
.el source files -- not necessary to run XEmacs.

%description el -l pl
Pliki ¼ród³owe procedur w eLispie do XEmacsa.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/*
