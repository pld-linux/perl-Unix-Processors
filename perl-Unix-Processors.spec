#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unix
%define		pnam	Processors
Summary:	Unix::Processors - interface to processor (CPU) information
Summary(pl.UTF-8):	Unix::Processors - interfejs do informacji o procesorze (CPU)
Name:		perl-Unix-Processors
Version:	2.046
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Unix/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7f90211861d572172d969b9b9798afaa
URL:		http://search.cpan.org/dist/Unix-Processors/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 1.0-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides accessors to per-processor (CPU) information.
The object is obtained with the Unix::Processors::processors call in a
OS independent manner.

%description -l pl.UTF-8
Ten pakiet udostępnia funkcje dostępowe do informacji o procesorach
(CPU). Ten obiekt jest dostępny poprzez wywołanie
Unix::Processors::processors w sposób niezależny od systemu
operacyjnego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Unix/*.pm
%{perl_vendorarch}/Unix/Processors
%dir %{perl_vendorarch}/auto/Unix/Processors
%attr(755,root,root) %{perl_vendorarch}/auto/Unix/Processors/*.so
%{_mandir}/man3/*
