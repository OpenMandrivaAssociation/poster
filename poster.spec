%define snap 20060221

Summary:	PostScript Utilities
Name:		poster
Version:	0
Release:	%mkrel 0.%{snap}.9
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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0-0.20060221.8mdv2011.0
+ Revision: 667808
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0-0.20060221.7mdv2011.0
+ Revision: 607194
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0-0.20060221.6mdv2010.1
+ Revision: 519056
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0-0.20060221.5mdv2010.0
+ Revision: 426760
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0-0.20060221.4mdv2009.1
+ Revision: 319078
- use %%ldflags (P0)

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0-0.20060221.3mdv2009.0
+ Revision: 140735
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0-0.20060221.3mdv2008.1
+ Revision: 125558
- kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0-0.20060221.3mdv2008.0
+ Revision: 75355
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0-0.20060221.2mdv2008.0
+ Revision: 64174
- use the new System/Printing RPM GROUP

* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0-0.20060221.1mdv2008.0
+ Revision: 62626
- Import poster



* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0-0.20060221.1mdv2008.0
- initial Mandriva package

* Tue Feb 10 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-02-10 18:18:39 (48828)
- First package. Closes: #10483

* Tue Feb 10 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-02-10 18:16:45 (48824)
- Created package structure for poster.
