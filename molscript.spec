Summary:	MolScript is a tool for producing publication quality molecular images.
URL:		http://www.avatar.se/molscript
Name:		molscript
Version:	2.1.2
Release:	1
Copyright:	*NOT DISTRIBUTABLE* 1997-1998 Per Kraulis.
Group:		Applications/Science
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	Mesa-devel libjpeg-devel zlib-devel libpng-devel gd-devel raster3d ImageMagick

%description
MolScript is one of the standard tools used for producing publication
quality molecular graphics images from 3D atomic coordinates,
particularly protein structures. The images can be produced in
Postscript (colour or black and white), Raster3D, VRML, RGB, JPEG, PNG
and GIF formats. The output can also be viewed interactively using X
windows with OpenGL. The software allows the representation of protein
secondary structure, alpha-helices and beta-strands, as smooth helical
ribbons or cylinders and smooth directional arrows respectively.

The MolScript source code, binaries and documentation cannot be
distributed freely as it is copyrighted 1997-1998 Per Kraulis. A
license is required to obtain and use the program, fortunately there
is no fee for academic institutions that use MolScript exclusively for
academic work. The licensed distribution package is available from
http://www.avatar.se/molscript

%description -l pl
MosScript jest jednym ze standardowych narzêdzi do tworzenia wysokiej jako¶ci molekularnych obrazów do pó¼niejszej póblikacji z trójwymiarowych koordunatów atomów. Obrazy mog± zostaæ wygenerowane w formatach: Postscipt (kolorowe i czarno bia³e), Raster3D, VRML, RGB, JPEG, PNG i GIF. Wyniki mo¿na równie¿ interaktynwnie ogl±daæ pod X'ami z OpenGL. 

Kod ¼ród³owy, binarki i dokumentacja nie mog± byæ rozpowszechniane za darmo, obowi±zuje zastrze¿enie. Wymagana jest licencja aby uzyskaæ i u¿ywaæ programu, na szczê¶cie nie ma op³at je¶li program u¿ywa siê w celach niekomercyjnych. Wersjê licencjonowan± mo¿na otrzymaæ pod adresem http://www.avatar.se/molscript

%prep
%setup -q
%patch -p1

%build
%{__make} COPT="$RPM_OPT_FLAGS"
cd examples
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 -s molauto molscript $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DISCLAIMER doc/ examples/
%attr(755,root,root) %{_bindir}/molauto
%attr(755,root,root) %{_bindir}/molscript
