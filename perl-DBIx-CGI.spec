%include	/usr/lib/rpm/macros.perl
Summary:	DBIx-CGI perl module
Summary(pl):	Modu� perla DBIx-CGI
Name:		perl-DBIx-CGI
Version:	0.01
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBIx/DBIx-CGI-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-15
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-DBI
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
DBIx-CGI - Easy to Use DBI interface for CGI scripts.

%description -l pl
DBIx-CGI - �atwy w u�yciu interfejs DBI dla skrypt�w CGI.

%prep
%setup -q -n DBIx-CGI-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/DBIx/CGI
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/DBIx/CGI.pm
%{perl_sitearch}/auto/DBIx/CGI

%{_mandir}/man3/*
