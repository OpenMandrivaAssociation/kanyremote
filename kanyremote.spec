Name:	kanyremote
Version:	6.1
Release:	2
Summary:	KDE frontend for anyRemote Wireless remote control program
License:	GPLv2+
Group:	Graphical desktop/KDE
BuildArch:	noarch
URL:	https://kde-apps.org/content/show.php/kAnyRemote?content=45047
Source0:		http://sourceforge.net/projects/anyremote/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:		%{name}.desktop
BuildRequires:	kde4-macros
BuildRequires:	desktop-file-utils
Requires:	python-kde4
Requires:	python-pybluez >= 0.9.1
Requires:	anyremote >= 5.4.1


%description
KDE front-end for anyremote Wireless remote control program.

%prep
%setup -q


%build
%configure2_5x --build=%{_host}
%make

%install
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%doc AUTHORS  ChangeLog  COPYING  README
%{_datadir}/pixmaps/*
%{_datadir}/applications/%{name}.desktop

