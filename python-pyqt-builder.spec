%define pname pyqt_builder

Name:		python-pyqt-builder
Version:	1.18.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/%{pname}/%{pname}-%{version}.tar.gz
Summary:	PyQt-builder is the PEP 517 compliant build system for PyQt and projects that extend PyQt
URL:		https://pypi.org/project/pyqt-builder/
License:	BSD-2-Clause
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildSystem:	python
BuildArch:	noarch

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that extend PyQt. It extends the SIP build system and uses Qt's qmake to perform the actual compilation and installation of extension modules.

%files
%{py_sitedir}/pyqtbuild
%{py_sitedir}/pyqt_builder-*.*-info
%{_bindir}/*
