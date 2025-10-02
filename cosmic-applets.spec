%undefine _debugsource_packages

%define         pkgname cosmic-applet
%define         bin cosmic-applet
%define         appname com.system76.Cosmic
%define         a11y AppletA11y
%define         applist AppList
%define         audio AppletAudio
%define         battery AppletBattery
%define         bluetooth AppletBluetooth
%define         inputsources AppletInputSources
%define         minimize AppletMinimize
%define         network AppletNetwork
%define         notifications AppletNotifications
%define         power AppletPower
%define         status AppletStatusArea
%define         tiling AppletTiling
%define         time AppletTime
%define         workspaces AppletWorkspaces
%define         appbutton PanelAppButton
%define         workspacesbutton PanelWorkspacesButton
%define         launcherbutton PanelLauncherButton
Name:           cosmic-applets
Version:        1.0.0
%define beta beta.1.1
Release:        %{?beta:0.%{beta}.}1
Summary:        Applets for COSMIC DE
Group:          Desktop/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-applets
Source0:        https://github.com/pop-os/cosmic-applets/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-icons

%package -n %{pkgname}-a11y
Summary:        %{summary}
Requires:       %{name} = %{version}

%description -n %{pkgname}-a11y
%{summary}.

%package -n %{pkgname}-app-list
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-app-list
%{summary}.

%package -n %{pkgname}-audio
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-audio
%{summary}.

%package -n %{pkgname}-battery
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-battery
%{summary}.

%package -n %{pkgname}-bluetooth
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-bluetooth
%{summary}.

%package -n %{pkgname}-input-sources
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-input-sources
%{summary}.

%package -n %{pkgname}-minimize
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-minimize
%{summary}.

%package -n %{pkgname}-network
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-network
%{summary}.

%package -n %{pkgname}-notifications
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-notifications
%{summary}.

%package -n %{pkgname}-power
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-power
%{summary}.

%package -n %{pkgname}-status-area
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-status-area
%{summary}.

%package -n %{pkgname}-tiling
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-tiling
%{summary}.

%package -n %{pkgname}-time
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-time
%{summary}.

%package -n %{pkgname}-workspaces
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-workspaces
%{summary}.

%package -n %{pkgname}-panel-button
Summary:        %{summary}
Requires:       %{name} = %{version}

%description -n %{pkgname}-panel-button
%{summary}.

%package -n %{pkgname}-launcher-button
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{name} = %{version}

%description -n %{pkgname}-launcher-button
%{summary}.

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/cosmic
%{_datadir}/metainfo/com.system76.CosmicApplets.metainfo.xml

%files -n %{pkgname}-a11y
%{_bindir}/cosmic-applet-a11y
%{_datadir}/applications/%{appname}%{a11y}.desktop

%files -n %{pkgname}-app-list
%{_bindir}/cosmic-app-list
%{_datadir}/applications/%{appname}%{applist}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{applist}.svg

%files -n %{pkgname}-audio
%{_bindir}/%{bin}-audio
%{_datadir}/applications/%{appname}%{audio}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{audio}-symbolic.svg

%files -n %{pkgname}-battery
%{_bindir}/%{bin}-battery
%{_datadir}/applications/%{appname}%{battery}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{battery}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-battery-*.svg

%files -n %{pkgname}-bluetooth
%{_bindir}/%{bin}-bluetooth
%{_datadir}/applications/%{appname}%{bluetooth}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{bluetooth}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-bluetooth-*.svg

%files -n %{pkgname}-input-sources
%{_bindir}/%{bin}-input-sources
%{_datadir}/applications/%{appname}%{inputsources}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{inputsources}-symbolic.svg

%files -n %{pkgname}-minimize
%{_bindir}/%{bin}-minimize
%{_datadir}/applications/%{appname}%{minimize}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{minimize}.svg

%files -n %{pkgname}-network
%{_bindir}/%{bin}-network
%{_datadir}/applications/%{appname}%{network}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{network}-symbolic.svg

%files -n %{pkgname}-notifications
%{_bindir}/%{bin}-notifications
%{_datadir}/applications/%{appname}%{notifications}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{notifications}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/cosmic-applet-notification-*.svg

%files -n %{pkgname}-power
%{_bindir}/%{bin}-power
%{_datadir}/applications/%{appname}%{power}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{power}-symbolic.svg

%files -n %{pkgname}-status-area
%{_bindir}/%{bin}-status-area
%{_datadir}/applications/%{appname}%{status}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{status}.svg

%files -n %{pkgname}-tiling
%{_bindir}/%{bin}-tiling
%{_datadir}/applications/%{appname}%{tiling}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{tiling}-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{tiling}.*.svg

%files -n %{pkgname}-time
%{_bindir}/%{bin}-time
%{_datadir}/applications/%{appname}%{time}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{time}-symbolic.svg

%files -n %{pkgname}-workspaces
%{_bindir}/%{bin}-workspaces
%{_datadir}/applications/%{appname}%{workspaces}.desktop
%{_datadir}/applications/%{appname}%{workspacesbutton}.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicAppletWorkspaces.svg
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{workspacesbutton}.svg

%files -n %{pkgname}-panel-button
%{_bindir}/cosmic-panel-button
%{_datadir}/applications/%{appname}%{appbutton}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{appbutton}.svg

%files -n %{pkgname}-launcher-button
%{_datadir}/applications/%{appname}%{launcherbutton}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}%{launcherbutton}.svg
