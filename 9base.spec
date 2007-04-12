Summary: 9base is a port of following original Plan 9 userland tools to Unix
Name: 9base
Version: 20051114
License: MIT
Release: %mkrel 3
Group: System/Base
URL: http://wmi.berlios.de/
Source: http://wmi.modprobe.de/snaps/9base-%version.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: gcc

%description
9base is a port of following original Plan 9 userland tools to Unix

%prep
%setup -q -n 9base-%version

%build
%make 

%install
%{__rm} -rf %{buildroot}
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
        mans=`echo $man | cut -d . -f 1`
        mv ${man} ${mans}9.1
done


%clean
%{__rm} -rf ${buildroot}

%files
%defattr(-,root,root)
%{_bindir}/9/*
%{_libdir}/rcmain
%{_mandir}/man1/*
%{_mandir}/man7/*

