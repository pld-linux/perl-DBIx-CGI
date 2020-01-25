%define		pdir	DBIx
%define		pnam	CGI
Summary:	DBIx::CGI Perl module - easy to Use DBI interface for CGI scripts
Summary(pl.UTF-8):	Moduł Perla DBIx::CGI - łatwy w użyciu interfejs DBI dla skryptów CGI
Name:		perl-DBIx-CGI
Version:	0.06
Release:	9
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c1c653b767f67608d073766e21c35522
Patch0:		%{name}-manpath.patch
URL:		http://search.cpan.org/dist/DBIx-CGI/
BuildRequires:	perl-DBI
BuildRequires:	perl-DBIx-Easy
BuildRequires:	perl-HTML-Parser >= 3.05
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::CGI Perl module is an easy to use DBI interface for CGI scripts.
Currently only the Pg, mSQL and MySQL drivers are supported.

%description -l pl.UTF-8
Moduł Perla DBIx::CGI stanowi łatwy w użyciu interfejs DBI dla
skryptów CGI. Aktualnie obsługiwane są jedynie starowniki Pg, mSQL i
MySQL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DBIx/CGI.pm
%{_mandir}/man3/*
