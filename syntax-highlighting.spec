%define major 5
%define libname %mklibname KF5SyntaxHighlighting %{major}
%define devname %mklibname KF5SyntaxHighlighting -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library for syntax highlighting
Name:		syntax-highlighting
Group:		Development/C++
Version:	5.29.0
License:	MIT
Url:		https://kde.org/
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Release:	1
BuildRequires:	cmake
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(ECM)
BuildRequires:	ninja

%description
Library for syntax highlighting

%files
%{_bindir}/kate-syntax-highlighter
%{_sysconfdir}/xdg/org_kde_ksyntaxhighlighting.categories

%package -n %{libname}
Summary:	Syntax highlighting library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Syntax highlighting library

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

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
