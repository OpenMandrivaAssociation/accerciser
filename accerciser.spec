Summary: An interactive Python tool for querying accessibility information
Name: accerciser
Version: 0.1.6
Release: %mkrel 1
Source0: http://download.gnome.org/sources/accerciser/%{name}-%{version}.tar.bz2
License: BSD
BuildRoot: %{_builddir}/%{name}-%{version}-rpmroot
Group: Accessibility
Url: http://live.gnome.org/Accerciser

BuildArch: noarch

BuildRequires: intltool
BuildRequires: gnome-doc-utils
Requires: gnome-python-gconf >= 2.12
Requires: gnome-python-desktop >= 2.14
Requires: pygtk2.0 >= 2.8
Requires: pygtk2.0-libglade >= 2.8
Requires: pyorbit >= 2.14
Requires: at-spi >= 1.7
Requires: gnome-python >= 2.12
Requires: gnome-python-bonobo >= 2.12
Requires: python-at-spi
Requires: ipython
Obsoletes: at-poke <= 0.2.3
Provides: at-poke

%description
An interactive Python accessibility explorer.

%prep
%setup -q

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib --sysconfdir=%_sysconfdir --disable-scrollkeeper --without-pyreqs
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%define gconf_schemas accerciser

%post
%post_install_gconf_schemas %gconf_schemas
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %gconf_schemas

%postun
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README NEWS 
%{_sysconfdir}/gconf/schemas/accerciser.schemas
%{_bindir}/accerciser
%{py_puresitedir}/accerciser
%{_datadir}/omf/accerciser/*
%{_datadir}/accerciser/*
%{_datadir}/icons/hicolor/*/apps/accerciser.*
%{_datadir}/applications/accerciser.desktop
