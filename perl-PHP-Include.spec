%define module	PHP-Include

Summary:	Include PHP files in Perl
Name:		perl-%{module}
Version:	0.2
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/E/ES/ESUMMERS/%{module}-%{version}.tar.bz2
Requires:	perl >= 5.004
BuildRequires:	perl-devel
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PHP::Include builds on the shoulders of Filter::Simple and Parse::RecDescent to
provide a Perl utility for including very simple PHP Files from a Perl program.

When working with Perl and PHP it is often convenient to be able to share
configuration data between programs written in both languages.  One solution to
this would be to use a language independent configuration file (did I hear
someone say XML?). Another solution is to use Perl's flexibility to read PHP
and rewrite it as Perl. PHP::Include does the latter with the help of
Filter::Simple and Parse::RecDescent to rewrite very simple PHP as Perl.

Filter::Simple is used to enable macros (at the moment only one) which 
cause PHP to be interpolated into your Perl source code, which is then parsed
using a Parse::RecDescent grammar to generate the appropriate Perl.

PHP::Include was designed to allow the more adventurous to add grammars that 
extend the complexity of PHP that may be included. 

%prep

%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/PHP
%{_mandir}/*/*


