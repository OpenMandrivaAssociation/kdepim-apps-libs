Name: kdepim-apps-libs
# Parts of this used to be in kdepim
Epoch:		3
Version:	20.08.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	2
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: Libraries used by KDE PIM applications
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: sasl-devel
BuildRequires: cmake(KF5AkonadiSearch)
BuildRequires: cmake(KF5AkonadiContact)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5GrantleeTheme)
BuildRequires: cmake(KF5WebKit)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(Qt5UiPlugin)
BuildRequires: cmake(KF5Libkleo)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5PimCommon)
BuildRequires: cmake(KF5Prison)
BuildRequires: cmake(QGpgme)
BuildRequires: cmake(Gpgmepp)
BuildRequires: cmake(Grantlee5)
BuildRequires: boost-devel
Obsoletes: %{mklibname KF5FollowupReminder 5} < %{epoch}:20.07.0-1
Obsoletes: %{mklibname KF5KdepimDBusInterfaces 5} < %{epoch}:20.07.0-1
Obsoletes: %{mklibname KF5SendLater 5} < %{epoch}:20.07.0-1

%description
Libraries used by KDE PIM applications.

%define major 5
%libpackage KF5KaddressbookGrantlee %{major}
%libpackage KF5KaddressbookImportExport %{major}

%define devname %{mklibname -d KF5PimAppsLibs}

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{mklibname KF5KaddressbookGrantlee %{major}} = %{EVRD}
Requires: %{mklibname KF5KaddressbookImportExport %{major}} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %name --all-name --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/kdepim-apps-lib.categories

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
