%define name libbeagle
%define version 0.3.5.1
%define release %mkrel 1
%define major 1
%define libname %mklibname beagle %major
%define develname %mklibname -d beagle

Summary: Beagle integration library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/beagle/%{name}-%{version}.tar.bz2
License: MIT/Apache License
Group: System/Libraries
Url: http://beagle-project.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk-doc
BuildRequires: glib2-devel
BuildRequires: pygtk2.0-devel

%description
Beagle is an indexing sub-system and search aggregator built on top of
Lucene.Net. It can index your files, mailboxes, your web browsing
behaviour and other things.

This is the shared library used to integrate beagle search in applications.

%package -n %libname
Group: System/Libraries
Summary: Shared library of beagle
%description -n %libname
Beagle is an indexing sub-system and search aggregator built on top of
Lucene.Net. 

%package -n %develname
Group: Development/C
Summary: Development library of beagle
Requires: %libname = %version
Provides: libbeagle-devel = %version-%release
Obsoletes: %mklibname -d beagle 0

%description -n %develname
Beagle is an indexing sub-system and search aggregator built on top of
Lucene.Net. 

%package -n python-beagle
Group: Development/Python
Summary: Python module for writing Beagle extensions
Requires: %libname = %version
Requires: pygtk2.0
%description -n python-beagle
Beagle is an indexing sub-system and search aggregator built on top of
Lucene.Net. 
Install this for python extensions to Beagle.

%prep
%setup -q 

%build
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %buildroot%_libdir/gtk-2.0/*/filesystems/libbeaglechooserhack*a \
      %buildroot%_libdir/%name/*a %buildroot%_libdir/python%pyver/site-packages/*a


%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%_includedir/libbeagle/
%_libdir/pkgconfig/libbeagle*.pc
%_datadir/gtk-doc/html/beagle/

%files -n python-beagle
%defattr(-,root,root)
%py_platsitedir/*beagle*


