Summary:	A *nix 'minimizer' for a few games
Summary(pl):	Aplikacja do minimalizowania okien gier
Name:		etswitch
Version:	0.1.13
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://hem.bredband.net/b400150/etswitch/%{name}-%{version}.tar.gz
# Source0-md5:	bc76ea975083c29098c3623398bed356
Patch0:		%{name}-desktop.patch
URL:		http://hem.bredband.net/b400150/
#BuildRequires:	X11-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Etswitch is a program allowing *nix users to minimize Enemy Territory
(and a plethora of other games) easily much in the same way as ETmin or
q3min for Windows users.

Aside from Wolf ET, etswitch also supports 21 other games available to
Linux users.

%description -l pl
Etswitch to program pozwalaj±cy u¿ytkownikom systemów uniksowych na
minimalizacjê Enemy Territory (oraz wielu innych gier) w ten sam
wygodny sposób jak aplikacje ETmin lub q3min dla u¿ytkowników systemów
Windows.

Oprócz Wolf ET etswitch obs³uguje 21 innych gier dostêpnych dla
u¿ytkowników Linuksa.

%prep
%setup -q
%patch0 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/etswitch
%{_mandir}/man1/etswitch.1*
%{_pixmapsdir}/*
%{_desktopdir}/*
