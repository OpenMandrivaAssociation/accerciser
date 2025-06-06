%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	An interactive Python tool for querying accessibility information
Name:		accerciser
Version:	3.46.2
Release:	2
Source0:	https://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
# Missing from 3.39.1 tarball; fixed in upstream git master            
Source1:        https://gitlab.gnome.org/GNOME/accerciser/-/raw/master/plugins/ipython_view.py
License:	BSD
Group:		Accessibility
Url:		https://live.gnome.org/Accerciser
BuildArch:	noarch
BuildRequires:  meson
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  appstream-util
BuildRequires:	pkgconfig(atspi-2) >= 2.1.5
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.1.13
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90.3
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(gnome-doc-utils) >= 0.17.3
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:	python-devel
BuildRequires:	itstool
BuildRequires:	yelp-tools
BuildRequires:  python3dist(ipython)

%description
An interactive Python accessibility explorer.

%prep
%autosetup -p1
# Missing from 3.39.1 tarball; fixed in upstream git master            
cp -a %{S:1} plugins/

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS README* NEWS 
%{_bindir}/%{name}
%{py_puresitedir}/%{name}
%_datadir/glib-2.0/schemas/org.a11y.Accerciser.gschema.xml
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/apps/%{name}-*
%{_datadir}/gnome-shell/extensions/accerciser@accerciser.gnome.org/extension.js
%{_datadir}/gnome-shell/extensions/accerciser@accerciser.gnome.org/metadata.json
%{_datadir}/metainfo/org.gtk.accerciser.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*
#{_datadir}/metainfo/*.appdata.xml
