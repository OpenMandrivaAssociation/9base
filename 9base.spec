%define debug_package	%{nil}

Summary: A port of following original Plan 9 userland tools to Unix
Name: 9base
Version: 6
License: MIT and Lucent Public License
Release: 2
Group: System/Base
URL: http://tools.suckless.org/9base
Source0: http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Source1: %{name}.rpmlintrc
Patch0: 9base-6-rosa-perms.patch
Patch1: 9base-6-rosa-etc.patch
BuildRequires: glibc-static-devel

%description
9base is a port of following original Plan 9 userland tools to Unix:
awk basename bc cat cleanname date echo grep rc sed seq sleep sort
tee test touch tr uniq

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%make 

%install
%{__make} DESTDIR=%{buildroot} PREFIX=%{_prefix}/ MANPREFIX=%{_mandir} \
		LIBDIR=%{_libdir}/9/ install

%ifarch x86_64
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
%endif

mkdir -p %{buildroot}%{_bindir}/9/
for file in %{buildroot}%{_bindir}/*
	do
	if [ -f $file ]; then
 	mv $file %{buildroot}%{_bindir}/9/
	fi
done
#grep awk sed bc basename cat date echo seq sleep sort tee test touch tr uniq
for man in `ls %{buildroot}%{_mandir}/man1/*.1`
do
        mans=`echo $man | sed 's/.1$/9.1/'`
        mv ${man} ${mans}
done

%post
echo "
if you want to use 9base, please add %{_bindir}/9 to your path:
export PATH=\$PATH:%{_bindir}/9"

%files
%{_bindir}/9/*
%{_libdir}/troff
%{_mandir}/man1/*
%{_sysconfdir}/rcmain


%changelog
* Thu May 31 2007 Antoine Ginies <aginies@mandriva.com> 20051114-4mdv2008.0
+ Revision: 33084
- adjust buildrequires
- add glibc-devel buildrequires
- fix bug #23957 (description and path)


* Sat Dec 10 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 20051114-3mdk
- fix build on x86_64
- fix debug files in main package

* Mon Dec 05 2005 Antoine Ginies <aginies@mandriva.com> 20051114-2mdk
- fix pb of man conflict

* Sat Dec 03 2005 Antoine Ginies <aginies@mandriva.com> 20051114-1mdk
- first release, need to create a subdir /usr/bin/9 to avoid conflict

