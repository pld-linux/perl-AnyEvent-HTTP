#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	AnyEvent
%define		pnam	HTTP
Summary:	AnyEvent::HTTP - simple but non-blocking HTTP/HTTPS client
Summary(pl.UTF-8):	AnyEvent::HTTP - prosty, nieblokujący klient HTTP/HTTPS
Name:		perl-AnyEvent-HTTP
Version:	2.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/AnyEvent/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a65ef37d987f65cd4340c611f4186013
URL:		http://search.cpan.org/dist/AnyEvent-HTTP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-AnyEvent >= 5.33
BuildRequires:	perl-common-sense >= 3.30
%endif
Requires:	perl-AnyEvent >= 5.33
Requires:	perl-common-sense >= 3.30
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a simple, stateless and non-blocking HTTP
client. It supports GET, POST and other request methods, cookies and
more, all on a very low level. It can follow redirects, supports
proxies, and automatically limits the number of connections to the
values specified in the RFC.

%description -l pl.UTF-8
Ten moduł jest implementacją prostego, bezstanowego i nieblokującego
klienta HTTP. Obsługuje GET, POST i inne metody żądań, ciasteczka itd.
na bardzo niskim poziomie. Potrafi podążać za przekierowaniami,
obsługuje proxy i automatycznie ogranicza liczbę połączeń do wartości
określonych w RFC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes README
%{perl_vendorlib}/AnyEvent/HTTP.pm
%{_mandir}/man3/AnyEvent::HTTP.3pm*
