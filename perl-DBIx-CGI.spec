%include	/usr/lib/rpm/macros.perl
Summary:	DBIx-CGI perl module
Summary(pl):	Modu³ perla DBIx-CGI
Name:		perl-DBIx-CGI
Version:	0.06
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBIx/DBIx-CGI-%{version}.tar.gz
Patch0:		perl-DBIx-CGI-manpath.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-DBI
BuildRequires:	perl-DBIx-Easy
BuildRequires:	perl-HTML-Parser >= 3.05
%requires_eq	perl
Requires:	%{perl_sitearch}
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
