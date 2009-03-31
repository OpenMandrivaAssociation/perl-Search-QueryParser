
%define realname   Search-QueryParser
%define version    0.93
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Parses a query string into a data structure
Source:     http://www.cpan.org/modules/by-module/Search/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

%description
This module parses a query string into a data structure to be handled by
external search engines. For examples of such engines, see the
File::Tabular manpage and the Search::Indexer manpage.

The query string can contain simple terms, "exact phrases", field names and
comparison operators, '+/-' prefixes, parentheses, and boolean connectors.

The parser can be parameterized by regular expressions for specific notions
of "term", "field name" or "operator" ; see the the new manpage method. The
parser has no support for lemmatization or other term transformations :
these should be done externally, before passing the query data structure to
the search engine.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


