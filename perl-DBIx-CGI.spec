%define	pdir	DBIx
%define	pnam	CGI
%include	/usr/lib/rpm/macros.perl
Summary:	DBIx-CGI perl module
Summary(pl):	Modu³ perla DBIx-CGI
Name:		perl-DBIx-CGI
Version:	0.06
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-manpath.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	perl-DBIx-Easy
BuildRequires:	perl-HTML-Parser >= 3.05
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx-CGI - Easy to Use DBI interface for CGI scripts.

%description -l pl
DBIx-CGI - ³atwy w u¿yciu interfejs DBI dla skryptów CGI.

%prep
%setup -q -n DBIx-CGI-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/DBIx/CGI.pm
%{_mandir}/man3/*
