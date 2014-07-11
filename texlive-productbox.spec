# revision 20886
# category Package
# catalog-ctan /macros/latex/contrib/gene/productbox
# catalog-date 2010-12-30 01:06:48 +0100
# catalog-license other-free
# catalog-version 1.1
Name:		texlive-productbox
Version:	1.1
Release:	8
Summary:	Typeset a three-dimensional product box
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gene/productbox
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/productbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/productbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/productbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables typesetting of a three-dimensional product
box. This product box can be rendered as it is standing on a
surface and some light is shed onto it. Alternatively it can be
typeset as a wireframe to be cut out and glued together. This
will lead to a physical product box. The package requires the
package pgf and TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/productbox/productbox.sty
%doc %{_texmfdistdir}/doc/latex/productbox/Makefile
%doc %{_texmfdistdir}/doc/latex/productbox/README
%doc %{_texmfdistdir}/doc/latex/productbox/productbox.bib
%doc %{_texmfdistdir}/doc/latex/productbox/productbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/productbox/productbox.dtx
%doc %{_texmfdistdir}/source/latex/productbox/productbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 755086
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719305
- texlive-productbox
- texlive-productbox
- texlive-productbox
- texlive-productbox

