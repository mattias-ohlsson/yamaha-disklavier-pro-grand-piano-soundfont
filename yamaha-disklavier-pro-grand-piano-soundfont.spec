Name:           yamaha-disklavier-pro-grand-piano-soundfont
Version:        20160804
Release:        1%{?dist}
Summary:        Acoustic grand piano sample library in SF2 format

License:        CC-BY
URL:            https://freepats.zenvoid.org/Piano/acoustic-grand-piano.html
Source0:        https://freepats.zenvoid.org/Piano/YDP-GrandPiano/YDP-GrandPiano-SF2-%{version}.tar.bz2

BuildArch:      noarch

%description
Acoustic grand piano sample library in SF2 format built from the Zenph Studios
Yamaha Disklavier Pro Piano Multisamples for OLPC.

%prep
%autosetup -n YDP-GrandPiano-SF2-%{version}

%build
mv YDP-GrandPiano-%{version}.sf2 YamahaDisklavierProGrandPiano.sf2

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/soundfonts/
install -p -m 644 YamahaDisklavierProGrandPiano.sf2 $RPM_BUILD_ROOT%{_datadir}/soundfonts/

%files
%doc YDP-GrandPiano-%{version}.txt
%{_datadir}/soundfonts/YamahaDisklavierProGrandPiano.sf2

%changelog
* Fri Jan 24 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 20160804-1
- Initial build
