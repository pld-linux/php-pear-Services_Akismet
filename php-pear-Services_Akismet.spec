%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Services_Akismet
Summary:	%{_pearname} - PHP client for the Akismet REST API
Summary(pl.UTF-8):	%{_pearname} - Klient PHP do API REST Akismet
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3340673e9b99e2171b9ecae7646f7903
URL:		http://pear.php.net/package/Services_Akismet/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Suggests:	php-curl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an object-oriented interface to the Akismet REST
API. Akismet is used to detect and to filter spam comments posted on
weblogs. Though the use of Akismet is not specific to Wordpress, you
will need a Wordpress API key from http://wordpress.com/api-keys/ to
use this package.

Akismet is free for personal use and a license may be purchased for
commercial or high-volume applications.

This package is derived from the miPHP Akismet class written by Bret
Kuhns for use in PHP 4. This package requires PHP 5.2.1.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dostarcza zorientowanego obiektowo interfejsu do API REST
Akismet, wykorzystywanego do wykrywania i filtorwania spamów w
komentarzach do wpisów na blogach. Chociaż wykorzystanie API jest
możliwe nie tylko z blogiem wordpress, do korzystania z tego pakietu
konieczne będzie pobranie klucza Wordpress API ze strony
http://wordpress.com/api-keys/ .

Akismet jest darmowe dla prywatnego użytku, licencję można nabyć dla
serwisów komercyjnych lub o dużym natężeniu ruchu.

Pakiet ten jest wzorowany na napisanej dla PHP 4 klasie miPHP Akismet,
której autorem jest Bret Kuhns.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Akismet
%{php_pear_dir}/Services/Akismet.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_Akismet
