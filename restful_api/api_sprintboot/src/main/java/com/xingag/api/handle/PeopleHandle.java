package com.xingag.api.handle;

import com.xingag.api.common.SqlProvider;
import com.xingag.api.domain.People;
import org.apache.ibatis.annotations.*;

import java.util.List;

/***
 * MyBatis映射数据库查询与具体的方法
 *
 * 包含：增（@Insert）、删（@Delete）、改（@UpdateProvider）、查（@Select）
 */
@Mapper
public interface PeopleHandle {

    /***
     * 查询数据表中的所有记录
     * 对应SQL：select * from people
     * @return
     */
    @Select("SELECT * FROM PEOPLE")
    List<People> getAllPeople();

    /***
     * 查询数据表中的某一条记录
     * @param id 查询的id
     * @return
     */
    @Select("SELECT * FROM PEOPLE where ID = #{id}")
    People getPeople(@Param("id") int id);

    /***
     * 插入一条数据
     * @param name 姓名
     * @param age  年龄
     * @param extra  其他
     * @return
     */
    @Insert("INSERT INTO PEOPLE(NAME,AGE,EXTRA) VALUES(#{name},#{age},#{extra})")
    int insertPeople(@Param("name") String name, @Param("age") int age, @Param("extra") boolean extra);


    /***
     * 更新一条记录（@UpdateProvider）
     * @param people 准备更新进去的数据
     * @return
     */
    @UpdateProvider(type = SqlProvider.class, method = "updatePeopleSql")
    int updatePeople(People people);

    /***
     * 删除某条记录（@Delete）
     * @param id 根据ID去删除一条记录
     * @return
     */
    @Delete("DELETE FROM PEOPLE WHERE ID = #{id}")
    int deletePeople(@Param("id") int id);

}
