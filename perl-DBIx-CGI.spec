%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	CGI
Summary:	DBIx::CGI perl module
Summary(pl):	Modu� perla DBIx::CGI
Name:		perl-DBIx-CGI
Version:	0.06
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-manpath.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	perl-DBIx-Easy
BuildRequires:	perl-HTML-Parser >= 3.05
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::CGI - Easy to Use DBI interface for CGI scripts.

%description -l pl
DBIx::CGI - �atwy w u�yciu interfejs DBI dla skrypt�w CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/DBIx/CGI.pm
%{_mandir}/man3/*
