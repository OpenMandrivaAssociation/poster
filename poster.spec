%define snap 20060221

Summary:	PostScript Utilities
Name:		poster
Version:	0
Release:	0.%{snap}.9
License:	GPLv2
Group:		System/Printing
Source0:	ftp://ftp.kde.org/pub/kde/printing/poster.tar.bz2
Patch0:		poster-LDFLAGS.diff

%description
Poster can be used to create a large poster by building it from multiple pages
and/or printing it on large media. It expects as input a generic (encapsulated)
postscript file, normally printing on a single page. The output is again a
postscript file, maybe containing multiple pages together building the poster.
The output pages bear cutmarks and have slightly overlapping images for easier
assembling. The input picture will be scaled to obtain the desired size.

%prep
%setup -qn %{name}-%{snap}
%patch0 -p0

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 poster %{buildroot}%{_bindir}/
install -m0644 poster.1 %{buildroot}%{_mandir}/man1/

%files
%doc COPYING ChangeLog README manual.ps
%attr(0755,root,root) %{_bindir}/poster
%attr(0644,root,root) %{_mandir}/man1/poster.1*

