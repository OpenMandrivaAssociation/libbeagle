%define name libbeagle
%define version 0.3.9
%define release 6
%define major 1
%define libname %mklibname beagle %major
%define develname %mklibname -d beagle
%define pyver 2.7

Summary: Beagle integration library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch1: libbeagle-0.3.5.1-fix-str-fmt.patch
Patch2: libbeagle-0.3.9-linkage.patch
Patch3: libbeagle-0.3.9-remove-duplicated-file-from-makefile.patch
License: MIT/Apache License
Group: System/Libraries
Url: https://beagle-project.org/
BuildRequires: gtk-doc docbook-dtd412-xml
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
%patch1 -p0
%patch2 -p1
%patch3 -p1
#gw needed by patch 2 and 3
autoreconf -fi

%build
%configure2_5x --enable-gtk-doc
%make

%install
%makeinstall_std

#gw bug in 0.3.9
%if %_lib != lib
mv %buildroot%_prefix/lib/python%pyver %buildroot%_libdir
%endif

rm -f %buildroot%_libdir/gtk-2.0/*/filesystems/libbeaglechooserhack*a \
      %buildroot%_libdir/%name/*a %buildroot%_libdir/python%pyver/site-packages/*a


%files -n %libname
%doc ChangeLog AUTHORS README INSTALL
%_libdir/lib*.so.%{major}*

%files -n %develname
%doc ChangeLog AUTHORS README INSTALL
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%_includedir/libbeagle/
%_libdir/pkgconfig/libbeagle*.pc
%_datadir/gtk-doc/html/beagle/

%files -n python-beagle
%doc ChangeLog AUTHORS README INSTALL
%py_platsitedir/*beagle*




