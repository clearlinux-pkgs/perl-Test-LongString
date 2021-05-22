#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-LongString
Version  : 0.17
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/R/RG/RGARCIA/Test-LongString-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RG/RGARCIA/Test-LongString-0.17.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-longstring-perl/libtest-longstring-perl_0.17-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-LongString-license = %{version}-%{release}
Requires: perl-Test-LongString-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Test::LongString v0.17
======================
A library to test long strings.
INSTALLATION

%package dev
Summary: dev components for the perl-Test-LongString package.
Group: Development
Provides: perl-Test-LongString-devel = %{version}-%{release}
Requires: perl-Test-LongString = %{version}-%{release}

%description dev
dev components for the perl-Test-LongString package.


%package license
Summary: license components for the perl-Test-LongString package.
Group: Default

%description license
license components for the perl-Test-LongString package.


%package perl
Summary: perl components for the perl-Test-LongString package.
Group: Default
Requires: perl-Test-LongString = %{version}-%{release}

%description perl
perl components for the perl-Test-LongString package.


%prep
%setup -q -n Test-LongString-0.17
cd %{_builddir}
tar xf %{_sourcedir}/libtest-longstring-perl_0.17-1.debian.tar.xz
cd %{_builddir}/Test-LongString-0.17
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Test-LongString-0.17/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-LongString
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Test-LongString/50c898db19b21728a7d5ce7db783b70f1a19ee4f
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::LongString.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-LongString/50c898db19b21728a7d5ce7db783b70f1a19ee4f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Test/LongString.pm
