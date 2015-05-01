%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	An interactive Python tool for querying accessibility information
Name:		accerciser
Version:	3.14.0
Release:	1
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
License:	BSD
Group:		Accessibility
Url:		http://live.gnome.org/Accerciser
BuildArch:	noarch
BuildRequires:	pkgconfig(atspi-2) >= 2.1.5
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.1.13
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90.3
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig(gnome-doc-utils) >= 0.17.3
BuildRequires:	python-devel
BuildRequires:	itstool

%description
An interactive Python accessibility explorer.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS README NEWS 
%{_bindir}/%{name}
%{py_puresitedir}/%{name}
%_datadir/glib-2.0/schemas/org.a11y.Accerciser.gschema.xml
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/HighContrast/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*
