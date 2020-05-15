%define major 5
%define libname %mklibname KF5SyntaxHighlighting %{major}
%define devname %mklibname KF5SyntaxHighlighting -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library for syntax highlighting
Name:		syntax-highlighting
Group:		Development/C++
Version:	5.70.0
License:	MIT
Url:		https://kde.org/
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Release:	1
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5XmlPatterns)
BuildRequires:	cmake(ECM)
# For QCH format docs
BuildRequires:	doxygen
BuildRequires:	qt5-assistant

%description
Library for syntax highlighting.

%files -f syntaxhighlighting5_qt.lang
%{_bindir}/kate-syntax-highlighter
%{_datadir}/qlogging-categories5/ksyntaxhighlighting.categories

%package -n %{libname}
Summary:	Syntax highlighting library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Syntax highlighting library.

%files -n %{libname}
%{_libdir}/libKF5SyntaxHighlighting.so.%{major}*

%package -n %{devname}
Summary:	Syntax highlighting development files
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for applications that use %{name}.

%files -n %{devname}
%{_includedir}/KF5/KSyntaxHighlighting
%{_includedir}/KF5/ksyntaxhighlighting_version.h
%{_libdir}/libKF5SyntaxHighlighting.so
%{_libdir}/cmake/KF5SyntaxHighlighting
%{_libdir}/qt5/mkspecs/modules/qt_KSyntaxHighlighting.pri

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
ls %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/*.qm |while read r; do
	F="$(echo $r |sed -e 's,%{buildroot},,')"
	L="$(echo $F |cut -d/ -f5)"
	echo "%%lang($L) $F" >>syntaxhighlighting5_qt.lang
done
