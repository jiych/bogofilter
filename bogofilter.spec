Summary:	Bayesian Spam Filter
Summary(pl):	Bayesja�ski Filtr Antyspamowy
Name:		bogofilter
Version:	0.7
Release:	1
License:	GPL
Group:		Applications/Mail
Vendor:		Eric S. Raymond <esr@thyrsus.com>
Source0:	http://www.tuxedo.org/~esr/bogofilter/%{name}-%{version}.tar.gz
URL:		http://www.tuxedo.org/~esr/bogofilter/
BuildRequires:	judy-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bogofilter is a Bayesian spam filter. In its normal mode of operation,
it takes an email message or other text on standard input, does a
statistical check against lists of "good" and "bad" words, and returns
a status code indicating whether or not the message is spam.
Bogofilter is designed with fast algorithms (including Berkeley DB
system), coded directly in C, and tuned for speed, so it can be used
for production by sites that process a lot of mail.

%description -l pl
Bogofilter jest bajesja�skim filtrem antyspamowym. W podstawowym
trybie dzia�ania na emailu lub innym tek�cie odczytanym na wej�ciu
wykonuje statystyczne testy na wyst�powanie "dobrych" i "z�ych" s��w i
zwraca kod powrotu wskazuj�cy czy wiadomo�� jest spamem, czy te� nie.
Bogofilter jest zaprojektowany z u�yciem szybkich algorytm�w
(w�aczaj�c w to Berkeley DB), napisany w czystym C i "podkr�cony" pod
k�tek szybko�ci, a wi�c mo�e by� u�ywany na systemach "produkcyjnych",
kt�re przetwarzaj� du�e ilo�ci poczty.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS TODO
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man1/*
