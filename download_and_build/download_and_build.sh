#!/bin/bash
# vim:set shiftwidth=4 softtabstop=4 expandtab:

bspwm_version=0.9.2
sxhkd_version=0.5.7
lemon_version=a43b801 
sutils_version=f35ea44
xtitle_version=0.3


function cleanup() {
    if [ "$#" -ne 1 ]; then
        echo "Illegal number of parameters";
        exit;
    fi
    echo "Cleanup $1"
    cd $1
    rm ./*.tar.gz 2> /dev/null
    rm ./.build*.log 2> /dev/null
    rm -rf ./$1-* 2> /dev/null
    rm -rf x86_64/ 2> /dev/null
    cd ..
}

if [ ! -e ./dist ]; then
    mkdir ./dist
fi

echo
echo
echo "Download prerequisites and dependencies"
read -s -r -p "Press space or enter to continue, x to exit, anything else to skip " -n1 key
echo
if [ "$key" = '' ]; then
    sudo dnf -y groupinstall "Development Tools"
    sudo dnf -y install libXft-devel libX11-devel libxcb-devel \
            xcb-util-devel xcb-util-wm-devel xcb-util-keysyms-devel \
            fedpkg alsa-lib-devel
elif [ "$key" = 'x' ]; then
    exit
fi


echo
echo
echo "Download and build bspwm"
read -s -r -p "Press space or enter to continue, x to exit, anything else to skip " -n1 key
echo
if [ "$key" = '' ]; then
    cd bspwm
    sed -i "s/Version:.*/Version:\t$bspwm_version/" bspwm.spec
    wget https://github.com/baskerville/bspwm/archive/$bspwm_version.tar.gz
    fedpkg --dist f23 local 
    cp ./x86_64/bspwm-$bspwm_version*.x86_64.rpm ../dist/
    cd ..
elif [ "$key" = 'x' ]; then
    exit
fi


echo
echo
echo "Download and build sxhkd"
read -s -r -p "Press space or enter to continue, x to exit, anything else to skip " -n1 key
echo
if [ "$key" = '' ]; then
    cd sxhkd
    sed -i "s/Version:.*/Version:\t$sxhkd_version/" sxhkd.spec
    wget https://github.com/baskerville/sxhkd/archive/$sxhkd_version.tar.gz
    fedpkg --dist f23 local 
    cp ./x86_64/sxhkd-$sxhkd_version*.x86_64.rpm ../dist/
    cd ..
elif [ "$key" = 'x' ]; then
    exit
fi


echo
echo
echo "Download and build lemonbar"
read -s -r -p "Press space or enter to continue, x to exit, anything else to skip " -n1 key
echo
if [ "$key" = '' ]; then
    cd lemonbar
    sed -i "s/Version:.*/Version:\t$lemon_version/" lemonbar.spec
    wget https://github.com/krypt-n/bar/archive/$lemon_version.tar.gz
    # This aint pretty, but it should work
    tar zxf $lemon_version.tar.gz
    mv bar-$lemon_version* lemonbar-$lemon_version
    mv $lemon_version.tar.gz downloaded.tar.gz
    tar zcf $lemon_version.tar.gz lemonbar-$lemon_version
    fedpkg --dist f23 local
    cp ./x86_64/lemonbar-$lemon_version*.x86_64.rpm ../dist/
    cd ..
elif [ "$key" = 'x' ]; then
    exit
fi


echo
echo
echo "Download and build sutils"
read -s -r -p "Press space or enter to continue, x to exit, anything else to skip " -n1 key
echo
if [ "$key" = '' ]; then
    cd sutils
    sed -i "s/Version:.*/Version:\t$sutils_version/" sutils.spec
    wget https://github.com/baskerville/sutils/archive/$sutils_version.tar.gz
    # This aint pretty, but it should work
    tar zxf $sutils_version.tar.gz
    mv sutils-$sutils_version* sutils-$sutils_version
    mv $sutils_version.tar.gz downloaded.tar.gz
    tar zcf $sutils_version.tar.gz sutils-$sutils_version
    fedpkg --dist f23 local
    cp ./x86_64/sutils-$sutils_version*.x86_64.rpm ../dist/
    cd ..
elif [ "$key" = 'x' ]; then
    exit
fi


echo
echo
echo "Download and build xtitle"
read -s -r -p "Press space or enter to continue, x to exit, anything else to skip " -n1 key
echo
if [ "$key" = '' ]; then
    cd xtitle
    sed -i "s/Version:.*/Version:\t$xtitle_version/" xtitle.spec
    wget https://github.com/baskerville/xtitle/archive/$xtitle_version.tar.gz
    fedpkg --dist f23 local 
    cp ./x86_64/xtitle-$xtitle_version*.x86_64.rpm ../dist/
    cd ..
elif [ "$key" = 'x' ]; then
    exit
fi


echo
echo
echo "Cleanup build directories"
read -s -r -p "Press space or enter to continue, x to exit, anything else to skip " -n1 key
echo
if [ "$key" = '' ]; then
    cleanup bspwm
    cleanup sxhkd
    cleanup lemonbar
    cleanup sutils
    cleanup xtitle
elif [ "$key" = 'x' ]; then
    exit
fi


echo
echo
echo "Create short named tar archive for easy copy to dom0"
read -s -r -p "Press space or enter to continue, x to exit, anything else to skip " -n1 key
echo
if [ "$key" = '' ]; then
    tar zcvf dist.tar.gz ./dist/
elif [ "$key" = 'x' ]; then
    exit
fi
