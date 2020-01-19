Name:           yamaha-disklavier-pro-grand-piano
Version:        
Release:        1%{?dist}
Summary:        

License:        
URL:            
Source0:        

BuildRequires:  
Requires:       

%description


%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Sun Jan 19 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com>
- 
