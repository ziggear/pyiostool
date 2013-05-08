#显示信息
xcodebuild -version
xcodebuild -list
xcrun      -version

#建立渠道数组
channels=([1]=91  [2]=weiphone [3]=tongbu [4]=tgbus [5]=jike [6]=shoujizhijia [7]=maoren8 [8]=25pp [9]=beike [10]=kuaiapp [11]=kuaiyong [12]=baixinshouji)
space=" "

#创建目录
mkdir build
mkdir build/release
chmod 755 -R build/

echo "channel list:"
for((i=1;i<=12;i++));
  do echo channel$i - ${channels[$i]};
     mkdir build/release/${channels[$i]};
  done

#准备build环境
xcodebuild clean -configuration Release
export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer/


#环境变量
arch="armv7"
targetName="MovieCoupon2"
projectName=${targetName}
productName="MovieCoupon"
mkdir ~/Desktop/${productName}
chmod 755 -R ~/Desktop/${productName}
version="2.5.0"
sign="iPhone Distribution: Beijing BuDingFangZhou Technology Co.,Ltd (DQZMZNN6Q9)"

#开始build
for((i=1;i<=12;i++));
do currChannelID=${channels[$i]};
   ipaPath=${productName}_${version}_${currChannelID}.ipa;
   distDir="build/release/${channels[$i]}"
   echo will building in ${distDir};
   #查找和替换相应参数 
   sed 's/moviecoupon_iPhone.*$/moviecoupon_iPhone_'${channels[$i]}'"/' ${targetName}/Global/Config.h > newConfig_${channels[$i]}.h
   cp newConfig_${channels[$i]}.h ${targetName}/Global/Config.h

   xcodebuild -configuration Release -target ${targetName} -sdk iphoneos6.1 -arch ${arch} build SYMROOT=${distDir} DSTROOT=${distDir};

   xcrun -sdk iphoneos6.1 PackageApplication -v ${distDir}/Release-iphoneos/${productName}.app -o "~/Desktop/${productName}/${ipaPath}" ;
done

#清理
#rm -rf build
#rm -rf *.h

echo **** building done ****
