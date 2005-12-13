Summary:	Bayesian Spam Filter
Summary(pl):	Bayesowski Filtr Antyspamowy
Name:		bogofilter
Version:	1.0.0
Release:	2
License:	GPL v2
Vendor:		Eric S. Raymond <esr@thyrsus.com>
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/bogofilter/%{name}-%{version}.tar.gz
# Source0-md5:	1f3bff28f7d9cb7b0c3a28184c101b53
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-dummy.patch
URL:		http://bogofilter.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	flex
BuildRequires:	gsl-devel
BuildRequires:	judy-devel
Requires:	gsl >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	-fomit-frame-pointer

%description
Bogofilter is a Bayesian spam filter. In its normal mode of operation,
it takes an email message or other text on standard input, does a
statistical check against lists of "good" and "bad" words, and returns
a status code indicating whether or not the message is spam.
Bogofilter is designed with fast algorithms (including Berkeley DB
system), coded directly in C, and tuned for speed, so it can be used
for production by sites that process a lot of mail.

%description -l pl
Bogofilter jest bayesowski filtrem antyspamowym. W podstawowym trybie
dzia�ania na emailu lub innym tek�cie odczytanym na wej�ciu wykonuje
statystyczne testy na wyst�powanie "dobrych" i "z�ych" s��w i zwraca
kod powrotu wskazuj�cy czy wiadomo�� jest spamem, czy te� nie.
Bogofilter jest zaprojektowany z u�yciem szybkich algorytm�w
(w��czaj�c w to Berkeley DB), napisany w czystym C i "podkr�cony" pod
k�tem szybko�ci, a wi�c mo�e by� u�ywany na systemach "produkcyjnych",
kt�re przetwarzaj� du�e ilo�ci poczty.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp $RPM_BUILD_ROOT%{_sysconfdir}/bogofilter.cf.example $RPM_BUILD_ROOT%{_sysconfdir}/bogofilter.cf

rm -f $RPM_BUILD_ROOT%{_bindir}/lexertest

%clean
rm -rf $RPM_BUILD_ROOT

%post

%banner %{name} -e <<'EOF'

WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING
------------------------------------------------------------------------
POTENTIAL FOR DATA CORRUPTION DURING UPDATES

If you plan to upgrade your database library, if only as a side effect
of an operating system upgrade, DO HEED the relevant documentation, for
instance, the /usr/share/doc/%{name}-%{version}/README.db file.  
You may need to prepare the upgrade with the old version of the software.

Otherwise, you may cause irrecoverable damage to your databases.

DO backup your databases before making the upgrade.
------------------------------------------------------------------------
WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING

EOF

#.

%files
%defattr(644,root,root,755)
%doc AUTHORS GETTING.STARTED RELEASE* NEWS README doc/README.db TODO
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/bogofilter.cf
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man1/*
