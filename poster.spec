%define snap 20060221

Summary:	PostScript Utilities
Name:		poster
Version:	0
Release:	%mkrel 0.%{snap}.6
License:	GPL
Group:		System/Printing
Source0:	ftp://ftp.kde.org/pub/kde/printing/poster.tar.bz2
Patch0:		poster-LDFLAGS.diff
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Poster can be used to create a large poster by building it from multiple pages
and/or printing it on large media. It expects as input a generic (encapsulated)
postscript file, normally printing on a single page. The output is again a
postscript file, maybe containing multiple pages together building the poster.
The output pages bear cutmarks and have slightly overlapping images for easier
assembling. The input picture will be scaled to obtain the desired size.

%prep

%setup -q -n %{name}-%{snap}
%patch0 -p0

%build

%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 poster %{buildroot}%{_bindir}/
install -m0644 poster.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README manual.ps
%attr(0755,root,root) %{_bindir}/poster
%attr(0644,root,root) %{_mandir}/man1/poster.1*
