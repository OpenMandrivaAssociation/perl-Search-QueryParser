%define upstream_name    Search-QueryParser
%define upstream_version 0.94

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Parses a query string into a data structure
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Search/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.940.0-2mdv2011.0
+ Revision: 658408
- rebuild for updated rpm-setup

* Thu Oct 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.940.0-1mdv2010.0
+ Revision: 451997
- update to 0.94

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.930.0-1mdv2010.0
+ Revision: 401612
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93-2mdv2010.0
+ Revision: 375903
- rebuild

* Tue Mar 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93-1mdv2009.1
+ Revision: 362905
- import perl-Search-QueryParser


* Tue Mar 31 2009 cpan2dist 0.93-1mdv
- initial mdv release, generated with cpan2dist

