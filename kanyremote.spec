Name:		kanyremote
Version:	6.0
Release:	1
Summary:	KDE frontend for anyRemote Wireless remote control program
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildArch:	noarch
URL:		http://kde-apps.org/content/show.php/kAnyRemote?content=45047
Source0:	http://sourceforge.net/projects/anyremote/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Requires:	python-kde4
Requires:	python-pybluez >= 0.9.1
Requires:	anyremote >= 5.4.1
BuildRequires:	kde4-macros
BuildRequires:	desktop-file-utils

%description
KDE front-end for anyremote Wireless remote control program.

%prep
%setup -q

%build
%configure2_5x --build=%{_host}
%make

%install
%makeinstall_std

desktop-file-install \
 --dir=%{buildroot}%{_datadir}/applications \
 --remove-category='Utility' \
 --add-category='System' \
 --add-category="KDE" \
 --add-category='Qt' \
 --add-category='HardwareSettings' \
 --remove-key='X-Desktop-File-Install-Version' \
 --remove-key='OnlyShowIn' \
 %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_docdir}/%{name}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/%{name}.desktop

