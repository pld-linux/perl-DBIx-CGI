%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	CGI
Summary:	DBIx::CGI perl module
Summary(pl):	Modu³ perla DBIx::CGI
Name:		perl-DBIx-CGI
Version:	0.06
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c1c653b767f67608d073766e21c35522
Patch0:		%{name}-manpath.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	perl-DBIx-Easy
BuildRequires:	perl-HTML-Parser >= 3.05
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::CGI - Easy to Use DBI interface for CGI scripts.

%description -l pl
DBIx::CGI - ³atwy w u¿yciu interfejs DBI dla skryptów CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DBIx/CGI.pm
%{_mandir}/man3/*
