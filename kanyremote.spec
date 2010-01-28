Summary: KDE4 frontend for anyRemote
Name: kanyremote
Version: 5.11.1
Release: %mkrel 1
License: GPLv2+
Group: Graphical desktop/KDE
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch
Source0: http://nchc.dl.sourceforge.net/sourceforge/anyremote/%name-%version.tar.gz
URL: http://anyremote.sourceforge.net/
Requires: python-kde4
Requires: python-pybluez

%description
kAnyRemote package is KDE GUI frontend for anyRemote written on PyKDE/PyQt.

%prep
%setup -q

%build
%configure2_5x --build=%{_host}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS README AUTHORS
%{_bindir}/%name
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
