#
# Conditional build:
%bcond_without	# do not perform "make test"
# 
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unix
%define		pnam	Processors
Summary:	Unix::Processors - interface to processor (CPU) information
Summary(pl):	Unix::Processors - interfejs do informacji o procesorze (CPU)
Name:		perl-Unix-Processors
Version:	2.030
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	12281477bf6d65c716c0644042f71e22
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides accessors to per-processor (CPU) information.
The object is obtained with the Unix::Processors::processors call in
a OS independent manner.

%description -l pl
Ten pakiet udostêpnia funkcje dostêpowe do informacji o procesorach
(CPU). Ten obiekt jest dostêpny poprzez wywo³anie
Unix::Processors::processors w sposób niezale¿ny od systemu
operacyjnego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/%{pdir}/*.pm
%{perl_vendorarch}/%{pdir}/%{pnam}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.so
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.bs
%{_mandir}/man3/*
