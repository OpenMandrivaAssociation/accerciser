Summary: An interactive Python tool for querying accessibility information
Name: accerciser
Version: 3.2.1
Release: 1
License: BSD
Group: Accessibility
Url: http://live.gnome.org/Accerciser
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildArch: noarch

BuildRequires:	GConf2
BuildRequires:	intltool
BuildRequires:	pkgconfig(atspi-2)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python)

%description
An interactive Python accessibility explorer.

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS README NEWS 
%{_bindir}/%{name}
%{py_puresitedir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.a11y.Accerciser.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/*

